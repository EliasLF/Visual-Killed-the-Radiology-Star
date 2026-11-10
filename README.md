# The Task

This project investigates the performance and interpretability of BiomedCLIP, a vision–language model for biomedical images, in text-to-image retrieval and image classification of radiological images.

We will evaluate the model using two datasets:

**ROCOv2** consists of radiology images paired with textual captions and expert-curated concepts drawn from a predefined vocabulary: https://zenodo.org/records/10821435

**BoghdadyJR/radiology** is derived from the original ROCO dataset and includes additional modality labels indicating the imaging technique used, such as MRI or X-ray: https://huggingface.co/datasets/BoghdadyJR/radiology


# The Model

**BiomedClip**

is a biomedical vision–language model that combines PubMedBERT as its text encoder with a Vision Transformer as its image encoder. It was pretrained on PMC-15M, a large-scale dataset of biomedical image–text pairs.
https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224
