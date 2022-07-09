import os


DATASET_PATH = "../data/test.txt"
labels=[]
def preprocess(dataset_path):
    # dictionary to store files
    
    # loop through all sub-folders
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # ensure we're processing at sub-folder level
        if dirpath is not dataset_path:

            # save label (i.e., sub-folder name) in the mapping eg SWH-05-20101106
            label = dirpath.split("/")[-1]
           
            print("\nProcessing: {}".format(label))

            # process all audio files in genre sub-dir
            for f in filenames:

		        # load audio file
                filename="wav/"+label+"/"+f
                labels.append(filename)
                                        
                                        
                 
if __name__ == "__main__":
    preprocess(DATASET_PATH)