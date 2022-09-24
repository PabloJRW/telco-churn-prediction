import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def catPlot(df, categorical):
    fig, ax = plt.subplots(nrows=5, ncols=3, figsize=(18,18))
    ax = ax.flatten()
    plt.suptitle('Categorical Variables', fontweight='bold', fontsize=24)

    for idx, var in enumerate(categorical):
        # Distribution Plots
        sns.countplot(x=df[var], hue=df.churn, ax=ax[idx])
        ax[idx].set_title((var + ' distribution').upper())
        ax[idx].set_xlabel(None)
        
    fig.tight_layout(h_pad=3)
    fig.savefig(os.path.join("..","img","cat_distributions.png"))
    plt.show()