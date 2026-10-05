import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


class BioprocessMonitor:
    def __init__(self, filepath, ph_lims, temperature_lims):
        self.filepath = filepath
        self.ph_lims = ph_lims
        self.temperature_lims = temperature_lims
        self.data = pd.read_csv(filepath)

    def extract_batch(self, batch_id):
        return self.data[self.data["batch_id"] == batch_id]
        #keeps data in rows where batch_id matches the request

    def optimal_ph_mask(self, df_batch):
        return(df_batch["pH"] >= self.ph_lims[0]) & (df_batch["pH"] <= self.ph_lims[1])
        #for showing which pH measurements are within acceptable range

    def optimal_temperature_mask(self, df_batch):
        return (df_batch["temperature_C"] >= self.temperature_lims[0]) & (df_batch["temperature_C"] <= self.temperature_lims[1])
        # for showing which temp measurements are within acceptable range

    def get_n_batches(self):
        return self.data["batch_id"].nunique()
        #to show how many batches are in dataset

    def export_dashboard(self, batch_id, filepath):
        df_batch = self.extract_batch(batch_id)
        #to get data from requested batch only

        ph_mask = self.optimal_ph_mask(df_batch)
        temperature_mask = self.optimal_temperature_mask(df_batch)
        #to differentiate between acceptable and not acceptable pH and temp data

        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6.5*2, 4.0*2), dpi=400, layout="constrained")
        #make 2x2 figure of plots
        #[0,0] = top left = [glucose], [biomass], [product] vs time
        #[0,1] = top right = temperature vs time
        #[1,0] = bottom left = pH vs time
        #[1,1] = bottom right = dissolved oxygen vs time

        kwargs_scatter = dict(s=35, edgecolor="black", alpha=0.7, linewidth=0.3)
        #to apply same format to all subplot markers

        #--------------------------------------------------
        # Glucose, biomass, & product concentration vs time
        # --------------------------------------------------
        axes[0, 0].scatter(
            df_batch["time_h"],
            df_batch["C_glucose_g_L^-1"],
            marker="o",
            color="purple",
            label="Glucose",
            **kwargs_scatter
        )
        #plot [glucose] vs time

        axes[0, 0].scatter(
            df_batch["time_h"],
            df_batch["C_biomass_g_L^-1"],
            marker="D",
            color="blue",
            label="Biomass",
            **kwargs_scatter
        )
        #plot [biomass] vs time

        axes[0, 0].scatter(
            df_batch["time_h"],
            df_batch["C_product_g_L^-1"],
            marker="*",
            color="deeppink",
            label="Product",
            **kwargs_scatter
        )
        #plot [product] vs time

        #add axis labels and legend
        axes[0, 0].set_xlabel("Time (h)")
        axes[0, 0].set_ylabel("Concentration (g/L)")
        axes[0, 0].legend()


        # --------------------------------------------------
        # Temperature vs time
        # --------------------------------------------------
        axes[0, 1].scatter(
            df_batch.loc[temperature_mask, "time_h"],
            df_batch.loc[temperature_mask, "temperature_C"],
            marker="o",
            color="green",
            label="Acceptable",
            **kwargs_scatter
        )
        #plots temp points in acceptable range

        axes[0, 1].scatter(
            df_batch.loc[~temperature_mask, "time_h"],
            df_batch.loc[~temperature_mask, "temperature_C"],
            marker="X",
            color="red",
            label="Outside range",
            **kwargs_scatter
        )
        #plots temp points outside acceptable range

        #axis labels and legen
        axes[0, 1].set_xlabel("Time (h)")
        axes[0, 1].set_ylabel("Temperature (°C)")
        axes[0, 1].legend()


        # --------------------------------------------------
        # pH vs time
        # --------------------------------------------------
        axes[1, 0].scatter(
            df_batch.loc[ph_mask, "time_h"],
            df_batch.loc[ph_mask, "pH"],
            marker="o",
            color="green",
            label="Acceptable",
            **kwargs_scatter
        )
        #plots pH pts in range

        axes[1, 0].scatter(
            df_batch.loc[~ph_mask, "time_h"],
            df_batch.loc[~ph_mask, "pH"],
            marker="X",
            color="red",
            label="Outside range",
            **kwargs_scatter
        )
        #plots pH pts outside range

        #axis labels and legend
        axes[1, 0].set_xlabel("Time (h)")
        axes[1, 0].set_ylabel("pH")
        axes[1, 0].legend()


        # --------------------------------------------------
        # Dissolved oxygen vs time
        # --------------------------------------------------
        axes[1, 1].scatter(
            df_batch["time_h"],
            df_batch["DO_percent"],
            marker="o",
            color="blue",
            **kwargs_scatter
        )
        #plot dissolved O2 vs time

        #axis labels
        axes[1, 1].set_xlabel("Time (h)")
        axes[1, 1].set_ylabel("Dissolved Oxygen (%)")

        #to add 6h ticks on all x-axes
        for ax in axes.flat:
            ax.xaxis.set_major_locator(MultipleLocator(6))

        fig.suptitle(f"Batch {batch_id}")

        plt.tight_layout()
        fig.savefig(filepath)
        plt.close(fig)
        #saves figure as .png and closes figure after saving

    def export_summary(self, filepath):
        summary = []
    #create summary table and export as .csv
        for batch_id in self.data["batch_id"].unique():
            df_batch = self.extract_batch(batch_id)

            ph_mask = self.optimal_ph_mask(df_batch)
            temperature_mask = self.optimal_temperature_mask(df_batch)

            ph_percent = ph_mask.mean() * 100
            temperature_percent = temperature_mask.mean() * 100

            final_product = df_batch["C_product_g_L^-1"].iloc[-1]

            summary.append({
                "batch_id": batch_id,
                "ph_optimal_percent": round(ph_percent, 2),
                "temperature_optimal_percent": round(temperature_percent, 2),
                "C_product_g_L^-1_final": final_product
            })

        summary_df = pd.DataFrame(summary)
        summary_df.to_csv(filepath, index=False)
