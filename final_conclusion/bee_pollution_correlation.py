import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

warnings.filterwarnings("ignore", category=FutureWarning)

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.dpi"] = 110
plt.rcParams["savefig.dpi"] = 130

DATA_DIR = Path.cwd()
BEE_CSV = DATA_DIR / "honey_bee_colonies_2025.csv"
POLL_CSV = DATA_DIR / "All Pollutant's Observation Changes from 2024 to 2025.csv"

QUARTER_ORDER = [
    "January-March 2024",
    "April-June 2024",
    "July-September 2024",
    "October-December 2024",
    "January-March 2025",
    "April-June 2025",
]
QUARTERS_2024 = QUARTER_ORDER[:4]

print("Bee CSV:", BEE_CSV.exists(), "|", BEE_CSV.stat().st_size, "bytes")
print("Pollutant CSV:", POLL_CSV.exists(), "|", round(POLL_CSV.stat().st_size / 1e6, 1), "MB")

bee_raw = pd.read_csv(BEE_CSV)
print("Shape:", bee_raw.shape)
print("Columns:", list(bee_raw.columns))
bee_raw.head()

print("Quarters:", bee_raw["Quarter"].unique().tolist())
print("State count:", bee_raw["State"].nunique())
print("Special state labels:", [s for s in bee_raw["State"].unique() if s in {"United States", "Other States"}])


def clean_numeric(series):
    return pd.to_numeric(
        series.astype(str).str.replace(r"\(X\)|\(Z\)", "", regex=True).replace("", np.nan),
        errors="coerce",
    )

bee = bee_raw.copy()
bee = bee[bee["State"] != "Other States"].copy()

for col in ["Colonies", "Max Colonies", "Lost", "Added", "Renovated", "Percent Lost", "Percent Renovated"]:
    bee[col] = clean_numeric(bee[col])

bee["Net Change"] = bee["Added"] - bee["Lost"]
bee["Net Change Rate (%)"] = 100 * bee["Net Change"] / bee["Max Colonies"]
bee["Turnover Rate (%)"] = 100 * (bee["Added"] + bee["Lost"]) / bee["Max Colonies"]

bee["Quarter"] = pd.Categorical(bee["Quarter"], categories=QUARTER_ORDER, ordered=True)
bee = bee.sort_values(["State", "Quarter"]).reset_index(drop=True)

print("After cleaning:", bee.shape)
bee.head()

bee.isna().sum().to_frame("missing").T

poll_raw = pd.read_csv(
    POLL_CSV,
    usecols=["State Name", "Parameter Name", "Observation Count", "Observation Percent",
             "Arithmetic Mean", "Quarter"],
    dtype={"State Name": "category", "Parameter Name": "category", "Quarter": "category"},
)
print("Shape:", poll_raw.shape)
print("Pollutants:", poll_raw["Parameter Name"].cat.categories.tolist())
print("Quarters:", poll_raw["Quarter"].cat.categories.tolist())
poll_raw.head()

poll = (
    poll_raw.groupby(["State Name", "Quarter", "Parameter Name"], observed=True)
    .agg(
        arithmetic_mean=("Arithmetic Mean", "mean"),
        observation_count=("Observation Count", "sum"),
        observation_percent=("Observation Percent", "mean"),
    )
    .reset_index()
)
poll = poll.rename(columns={"State Name": "State"})
poll["State"] = poll["State"].astype(str)
poll["Quarter"] = poll["Quarter"].astype(str)
poll["Parameter Name"] = poll["Parameter Name"].astype(str)
print("Aggregated shape:", poll.shape)
poll.head(10)

poll_wide = poll.pivot_table(
    index=["State", "Quarter"],
    columns="Parameter Name",
    values="arithmetic_mean",
).reset_index()
poll_wide.columns.name = None

POLLUTANT_COLS = [c for c in poll_wide.columns if c not in {"State", "Quarter"}]
print("Pollutant columns:", POLLUTANT_COLS)
poll_wide.head()

bee_states = bee[~bee["State"].isin(["United States"])].copy()
bee_states["Quarter"] = bee_states["Quarter"].astype(str)

panel = bee_states.merge(poll_wide, on=["State", "Quarter"], how="inner")
panel = panel[panel["Quarter"].isin(QUARTER_ORDER)].copy()
print("Merged panel shape:", panel.shape)
print("States in panel:", panel["State"].nunique())
print("Quarters in panel:", panel["Quarter"].unique().tolist())
panel.head()

us_bee = (
    bee[bee["State"] == "United States"][["Quarter", "Percent Lost", "Percent Renovated", "Net Change Rate (%)"]]
    .copy()
)
us_bee["Quarter"] = us_bee["Quarter"].astype(str)
us_bee = us_bee[us_bee["Quarter"].isin(QUARTER_ORDER)].sort_values(
    "Quarter", key=lambda s: s.map({q: i for i, q in enumerate(QUARTER_ORDER)})
)
us_bee

us_poll = (
    poll_wide[poll_wide["Quarter"].isin(QUARTER_ORDER)]
    .groupby("Quarter")[POLLUTANT_COLS]
    .mean()
    .reindex(QUARTER_ORDER)
    .reset_index()
)
us_poll

timeline = us_bee.merge(us_poll, on="Quarter")
timeline["Quarter"] = pd.Categorical(timeline["Quarter"], categories=QUARTER_ORDER, ordered=True)
timeline = timeline.sort_values("Quarter").reset_index(drop=True)
timeline

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

ax = axes[0]
ax.plot(timeline["Quarter"].astype(str), timeline["Percent Lost"], marker="o", color="#c0392b", label="Percent Lost")
ax.plot(timeline["Quarter"].astype(str), timeline["Percent Renovated"], marker="s", color="#27ae60", label="Percent Renovated")
ax.plot(timeline["Quarter"].astype(str), timeline["Net Change Rate (%)"], marker="^", color="#2980b9", label="Net Change Rate")
ax.set_ylabel("Percent of max colonies")
ax.set_title("US honeybee colony dynamics, 2024 - 2025")
ax.legend(loc="best")

ax = axes[1]
for col in POLLUTANT_COLS:
    series = timeline[col]
    norm = (series - series.min()) / (series.max() - series.min() + 1e-9)
    ax.plot(timeline["Quarter"].astype(str), norm, marker="o", label=col)
ax.set_ylabel("Pollutant level (min-max normalized)")
ax.set_title("US-average pollutant concentrations, 2024 -2025 (normalized for cross-pollutant comparison)")
ax.legend(loc="best", fontsize=8)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

def corr_block(df, x_cols, y_cols):
    rows = []
    for x in x_cols:
        for y in y_cols:
            sub = df[[x, y]].dropna()
            if len(sub) < 3:
                continue
            r, p = stats.pearsonr(sub[x], sub[y])
            rho, p_s = stats.spearmanr(sub[x], sub[y])
            rows.append({
                "bee_metric": x, "pollutant": y, "n": len(sub),
                "pearson_r": r, "pearson_p": p,
                "spearman_rho": rho, "spearman_p": p_s,
            })
    return pd.DataFrame(rows)

bee_metrics = ["Percent Lost", "Percent Renovated", "Net Change Rate (%)"]
timeline_corr = corr_block(timeline, bee_metrics, POLLUTANT_COLS)
timeline_corr.style.format({
    "pearson_r": "{:+.3f}", "pearson_p": "{:.3f}",
    "spearman_rho": "{:+.3f}", "spearman_p": "{:.3f}",
}).background_gradient(subset=["pearson_r"], cmap="RdBu_r", vmin=-1, vmax=1)

state_corr = corr_block(panel, bee_metrics, POLLUTANT_COLS)
state_corr["sig_pearson"] = state_corr["pearson_p"].apply(lambda p: "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "")
state_corr_sorted = state_corr.sort_values("pearson_p")
state_corr_sorted.style.format({
    "pearson_r": "{:+.3f}", "pearson_p": "{:.4f}",
    "spearman_rho": "{:+.3f}", "spearman_p": "{:.4f}",
}).background_gradient(subset=["pearson_r"], cmap="RdBu_r", vmin=-0.5, vmax=0.5)

heat = state_corr.pivot(index="bee_metric", columns="pollutant", values="pearson_r")
fig, ax = plt.subplots(figsize=(9, 3.2))
sns.heatmap(heat, annot=True, fmt="+.2f", cmap="RdBu_r", center=0, vmin=-0.5, vmax=0.5,
            cbar_kws={"label": "Pearson r"}, ax=ax)
ax.set_title("Pooled state × quarter correlations (2024-2025, n ≈ varies per pollutant)")
ax.set_xlabel("")
ax.set_ylabel("")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, len(POLLUTANT_COLS), figsize=(4 * len(POLLUTANT_COLS), 4), sharey=True)
for ax, pollutant in zip(axes, POLLUTANT_COLS):
    sub = panel[["Percent Lost", pollutant]].dropna()
    if sub.empty:
        ax.set_visible(False)
        continue
    sns.regplot(data=sub, x=pollutant, y="Percent Lost", ax=ax,
                scatter_kws={"alpha": 0.55, "s": 28, "color": "#34495e"},
                line_kws={"color": "#e67e22"})
    r, p = stats.pearsonr(sub[pollutant], sub["Percent Lost"])
    ax.set_title(f"{pollutant}\nr = {r:+.2f}, p = {p:.3f}, n = {len(sub)}", fontsize=10)
    ax.set_xlabel(pollutant)
axes[0].set_ylabel("Percent Lost (%)")
plt.suptitle("Honeybee Percent Lost vs. pollutant Arithmetic Mean (state × quarter, 2024-2025)", y=1.04)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, len(POLLUTANT_COLS), figsize=(4 * len(POLLUTANT_COLS), 4), sharey=True)
for ax, pollutant in zip(axes, POLLUTANT_COLS):
    sub = panel[["Net Change Rate (%)", pollutant]].dropna()
    if sub.empty:
        ax.set_visible(False)
        continue
    sns.regplot(data=sub, x=pollutant, y="Net Change Rate (%)", ax=ax,
                scatter_kws={"alpha": 0.55, "s": 28, "color": "#34495e"},
                line_kws={"color": "#16a085"})
    r, p = stats.pearsonr(sub[pollutant], sub["Net Change Rate (%)"])
    ax.set_title(f"{pollutant}\nr = {r:+.2f}, p = {p:.3f}, n = {len(sub)}", fontsize=10)
    ax.set_xlabel(pollutant)
axes[0].set_ylabel("Net Change Rate (%)")
plt.suptitle("Honeybee Net Change Rate vs. pollutant Arithmetic Mean (state × quarter, 2024-2025)", y=1.04)
plt.tight_layout()
plt.show()

state_summary = (
    panel.groupby("State", as_index=False)
    .agg(
        percent_lost=("Percent Lost", "mean"),
        net_change_rate=("Net Change Rate (%)", "mean"),
        **{f"{p}__mean": (p, "mean") for p in POLLUTANT_COLS},
    )
)
print("States with full panel coverage:", len(state_summary))
state_summary.head()

state_avg_corr_rows = []
for pollutant in POLLUTANT_COLS:
    col = f"{pollutant}__mean"
    for bee_col, label in [("percent_lost", "Percent Lost"), ("net_change_rate", "Net Change Rate (%)")]:
        sub = state_summary[[bee_col, col]].dropna()
        if len(sub) < 5:
            continue
        r, p = stats.pearsonr(sub[bee_col], sub[col])
        rho, p_s = stats.spearmanr(sub[bee_col], sub[col])
        state_avg_corr_rows.append({
            "bee_metric": label, "pollutant": pollutant, "n_states": len(sub),
            "pearson_r": r, "pearson_p": p,
            "spearman_rho": rho, "spearman_p": p_s,
        })
state_avg_corr = pd.DataFrame(state_avg_corr_rows).sort_values("pearson_p")
state_avg_corr.style.format({
    "pearson_r": "{:+.3f}", "pearson_p": "{:.4f}",
    "spearman_rho": "{:+.3f}", "spearman_p": "{:.4f}",
})

strongest = state_avg_corr.iloc[0]
pollutant = strongest["pollutant"]
fig, ax = plt.subplots(figsize=(9, 6))
sub = state_summary[["State", "percent_lost", f"{pollutant}__mean"]].dropna()
ax.scatter(sub[f"{pollutant}__mean"], sub["percent_lost"], s=55, color="#2c3e50", alpha=0.75)
for _, row in sub.iterrows():
    ax.annotate(row["State"], (row[f"{pollutant}__mean"], row["percent_lost"]),
                fontsize=8, alpha=0.8, xytext=(3, 3), textcoords="offset points")
slope, intercept, r, p, _ = stats.linregress(sub[f"{pollutant}__mean"], sub["percent_lost"])
xx = np.linspace(sub[f"{pollutant}__mean"].min(), sub[f"{pollutant}__mean"].max(), 100)
ax.plot(xx, slope * xx + intercept, color="#e74c3c", linewidth=1.5, label=f"OLS fit (r = {r:+.2f}, p = {p:.3f})")
ax.set_xlabel(f"{pollutant} — 2024-2025 mean concentration")
ax.set_ylabel("Mean Percent Lost across 2024-2025 (%)")
ax.set_title(f"State-level relationship: Percent Lost vs. {pollutant}")
ax.legend()
plt.tight_layout()
plt.show()

matrix_cols = bee_metrics + POLLUTANT_COLS
corr_matrix = panel[matrix_cols].corr(method="pearson")
mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt="+.2f", cmap="RdBu_r", center=0,
            vmin=-1, vmax=1, square=True, cbar_kws={"label": "Pearson r"}, ax=ax)
ax.set_title("Pearson correlation matrix (state × quarter pooled, 2024-2025)")
plt.tight_layout()
plt.show()