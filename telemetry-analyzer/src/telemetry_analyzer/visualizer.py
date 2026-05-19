import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generate_correlation_heatmap(correlations: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 8))

    heatmap = ax.imshow(correlations)

    ax.set_yticks(range(len(correlations.columns)))
    ax.set_xticks(range(len(correlations.columns)))

    ax.set_xticklabels(correlations.columns, rotation=45, ha="right")
    ax.set_yticklabels(correlations.columns)

    for i in range(len(correlations.columns)):
        for j in range(len(correlations.columns)):
            value = correlations.iloc[i, j]

            ax.text(
                j,
                i,
                f"{value:.2f}",
                ha="center",
                va="center",
            )

    ax.set_title("Service Error Correlation Heatmap")

    fig.colorbar(heatmap)

    plt.tight_layout()

    project_root = Path(__file__).resolve().parent.parent.parent
    output_path = project_root / "sample_data" / "service_correlation_heatmap.png"

    plt.savefig(output_path, dpi=300)

    print(f"Heatmap saved, please see {output_path}")

    plt.show()


