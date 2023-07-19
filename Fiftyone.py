import fiftyone as fo

# A name for the dataset
name = "my-dataset"
# The directory containing the dataset to import
dataset_dir = "./resources/"


dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.VOCDetectionDataset, # The type of the dataset being imported
    dataset_dir=dataset_dir,
    name=name,
)

if __name__=="__main__":
    # Ensures that the App processes are safely launched on Windows
    session = fo.launch_app(dataset)
    session.wait()



"""
# reference : https://docs.voxel51.com/user_guide/dataset_creation/datasets.html#vocdetectiondataset-import

import fiftyone as fo

name = "my-dataset"
dataset_dir = "/path/to/voc-detection-dataset"

# Create the dataset
dataset = fo.Dataset.from_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.VOCDetectionDataset,
    name=name,
)

# View summary info about the dataset
print(dataset)

# Print the first few samples in the dataset
print(dataset.head())

"""