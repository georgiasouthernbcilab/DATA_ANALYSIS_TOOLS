from collections import defaultdict
import os
import pandas as pd
import numpy as np

column_categories = ['Theta', 'Alpha', 'BetaL', 'BetaH', 'Gamma']
contactQuality = ['Timestamp', 'CQ', 'Overall']
electrode_locations = ['Timestamp', 'EEG.Cz', 'EEG.Fz', 'EEG.Fp1', 'EEG.F7', 'EEG.F3', 'EEG.FC1', 'EEG.C3', 'EEG.FC5', 'EEG.FT9', 'EEG.T7', 'EEG.CP5', 'EEG.CP1', 'EEG.P3', 'EEG.P7', 'EEG.PO9', 'EEG.O1', 'EEG.Pz', 'EEG.Oz', 'EEG.O2', 'EEG.PO10', 'EEG.P8', 'EEG.P4', 'EEG.CP2', 'EEG.CP6', 'EEG.T8', 'EEG.FT10', 'EEG.FC6', 'EEG.C4', 'EEG.FC2', 'EEG.F4', 'EEG.F8', 'EEG.Fp2']

class Operations:
    def compute_aggregated_statistics(self, df, categories=column_categories):
        aggregated_stats = {}
        for category in categories:
            # Combine all columns that match the brain wave category into a single series
            category_columns = [col for col in df.columns if col.split('.')[-1] == category]
            combined_data = df[category_columns].dropna().values.flatten()
            if len(combined_data) > 0:
                aggregated_stats[category] = {
                    'Average': np.mean(combined_data),
                    'Standard Deviation': np.std(combined_data),
                    'Min': np.min(combined_data),
                    'Max': np.max(combined_data),
                    'Number of Local Mins': len((np.diff(np.sign(np.diff(combined_data))) > 0).nonzero()[0]),
                    'Number of Local Maxes': len((np.diff(np.sign(np.diff(combined_data))) < 0).nonzero()[0])
                }
        return aggregated_stats

class Participant(Operations):
    def __init__(self, directory):
        self.directory = directory
        self.column_categories = column_categories
        self.process_directory()
        self.compute_all_aggregated_statistics()

    def _filter_columns(self, df, column_categories=column_categories):
        filtered_columns = [col for col in df.columns if any(category in col for category in self.column_categories)]
        return df[filtered_columns]

    def create_data_frame(self, file, filter=None):
        file_path = os.path.join(self.directory, file)
        df = pd.read_csv(file_path, skiprows=1)
        if filter:
            df = self._filter_columns(df, filter)
        df = df.dropna()
        return df

    def process_directory(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if "Baseline" in file:
                    self.baseline_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_1_excited_1_motorsports_kenMiles' in file:
                    self.excited_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_1_excited_2_sports_NBA' in file:
                    self.excited_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_1_excited_3_general_ratatChaseScene' in file:
                    self.excited_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_2_happy_scooby' in file:
                    self.happy_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_3_motivated_motivationalAuthor' in file:
                    self.motivated_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_4_relaxed_1_meditation_meditation' in file:
                    self.relaxed_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_4_relaxed_2_nature_waterfall' in file:
                    self.relaxed_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_4_relaxed_3_general_asmr' in file:
                    self.relaxed_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_5_sad_1_animals_saddogs' in file:
                    self.sad_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_5_sad_2_babies_sadBaby1' in file:
                    self.sad_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_5_sad_3_general_ChampDeath' in file:
                    self.sad_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_6_horror_conjuring' in file:
                    self.fearful_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_7_disgusted_trainspotting' in file:
                    self.disgust_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_8_angry_1_animals_angrydogs' in file:
                    self.angry_pow_df = self.create_data_frame(file, column_categories)
                elif 'From_videos_8_angry_2_general_thepiano' in file:
                    self.angry_pow_df = self.create_data_frame(file, column_categories)

    def compute_all_aggregated_statistics(self):
        dataframes = {
            'baseline_pow_df': self.baseline_pow_df,
            'excited_pow_df': self.excited_pow_df,
            'happy_pow_df': self.happy_pow_df,
            'motivated_pow_df': self.motivated_pow_df,
            'relaxed_pow_df': self.relaxed_pow_df,
            'sad_pow_df': self.sad_pow_df,
            'fearful_pow_df': self.fearful_pow_df,
            'disgust_pow_df': self.disgust_pow_df,
            'angry_pow_df': self.angry_pow_df
        }
        
        for name, df in dataframes.items():
            if df is not None:
                setattr(self, f'{name}_stats', self.compute_aggregated_statistics(df))


if __name__ == "__main__":
    participant1 = Participant(r'T:\GITHUB\DATA_ANALYSIS_TOOLS\103918\split')
    # print(participant1.angry_pow_df)
    print(participant1.angry_pow_df_stats)
    # Example of accessing the average of Theta for angry_pow_df
    # print(participant1.angry_pow_df_stats['Theta']['Average'])
