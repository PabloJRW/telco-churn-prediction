import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.color_palette("Paired", 9)

def numPlot(df, numerical):
    fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(18,12))
    ax = ax.flatten()
    plt.suptitle('Numerical Variables', fontweight='bold', fontsize=24)

    for idx, var in enumerate(numerical):
        # Distribution Plots
        sns.histplot(x=var,data=df, bins=50, kde=True, color="k", ax=ax[idx])
        ax[idx].set_title((var + ' distribution').upper())
        ax[idx].set_xlabel(None)
    
        # vs Churn --- Histograms
        sns.histplot(x=var,data=df, hue='churn', bins=50, kde=True, ax=ax[idx+3])
        ax[idx+3].set_title((var + ' vs Churn').upper())
        ax[idx+3].set_xlabel(None)
    
        # vs Churn --- Boxplots
        sns.boxplot(y=var, data=df, x='churn', ax=ax[idx+6])
        ax[idx+6].set_title((var + ' vs Churn').upper())
        ax[idx+6].set_xlabel(None)
        
    fig.tight_layout()
    plt.show()
