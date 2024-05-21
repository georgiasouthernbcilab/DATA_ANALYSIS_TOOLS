from collections import defaultdict
import os
import pandas as pd

column_categories = ['Theta', 'Alpha', 'BetaL', 'BetaH', 'Gamma']
# dataFrames = {'Theta':None,'Alpha':None,'BetaL':None,'BetaH':None,'Gamma':None}
dataFrameStatistics = {'Theta':None,'Alpha':None,'BetaL':None,'BetaH':None,'Gamma':None}
emotionStatistics = {'Happy':None,'Sad':None,'Angry':None,'Fearful':None,'Excited':None,'Disgust':None,'Motivated':None}
# Must keep certain things!  Rating is one!  Need to add rating!
# changeStatistics = {'Delta'}

# class Operations:

class Participant:
    def __init__(self, directory):
        self.directory = directory
        self.column_categories = column_categories
        self.baseline_stats = {}
        self.excited_stats = {}
        self.happy_stats = {}
        self.motivated_stats = {}
        self.relaxed_stats = {}
        self.sad_stats = {}
        self.fearful_stats = {}
        self.disgust_stats = {}
        self.angry_stats = {}
        self.process_directory()

    def _filter_columns(self, df,column_categories=column_categories):
        filtered_columns = [col for col in df.columns if any(category in col for category in self.column_categories)]# filtered_columns = [col for col in df.columns if any(category in col for category in column_categories)]
        return df[filtered_columns]

    def create_data_frame(self, file, filter = None):
        file_path = os.path.join(self.directory, file)
        df = pd.read_csv(file_path, skiprows=1)
        if filter:
            df = self._filter_columns(df,filter)
        df = df.dropna()
        return df

    def process_directory(self):
        # global root
        for root, dirs, files in os.walk(self.directory): #for root, dirs, files in os.walk(root):

            # print(files)# Insert a blank line in the output every time this function is called
            # Iterate through files in the current directory
            for file in files:

                if "Baseline" in file:## Note: Keep everything flexible by defining exactly for the videos
                    self.baseline_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_1_excited_1_motorsports_kenMiles' in file:
                    self.excited_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_1_excited_2_sports_NBA' in file:
                    self.excited_pow_df=self.create_data_frame(file,column_categories)

                elif 'From_videos_1_excited_3_general_ratatChaseScene' in file:
                    self.excited_pow_df=self.create_data_frame(file,column_categories)

                elif 'From_videos_2_happy_scooby' in file:
                    self.happy_pow_df=self.create_data_frame(file,column_categories)

                elif 'From_videos_3_motivated_motivationalAuthor' in file:
                    self.motivated_pow_df=self.create_data_frame(file,column_categories)

                elif 'From_videos_4_relaxed_1_meditation_meditation' in file:             
                    self.relaxed_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_4_relaxed_2_nature_waterfall' in file:                
                    self.relaxed_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_4_relaxed_3_general_asmr' in file:                 
                    self.relaxed_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_5_sad_1_animals_saddogs' in file:
                    self.sad_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_5_sad_2_babies_sadBaby1' in file:
                    self.sad_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_5_sad_3_general_ChampDeath' in file:                 
                    self.sad_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_6_horror_conjuring' in file:               
                    self.fearful_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_7_disgusted_trainspotting' in file:                 
                    self.disgust_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_8_angry_1_animals_angrydogs' in file:                 
                    self.angry_pow_df = self.create_data_frame(file,column_categories)

                elif 'From_videos_8_angry_2_general_thepiano' in file:                   
                    self.angry_pow_df = self.create_data_frame(file,column_categories)

if __name__ == "__main__":
    participant1 = Participant(r'T:\GITHUB\DATA_ANALYSIS_TOOLS\103918\split')
    print(participant1.angry_pow_df)