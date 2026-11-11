# Midpoint Reflection – Phase I: Experience with Generative AI

## AI-assisted Subgroup Members

- **Student 1:** Maria Boukhalfa Bennai  K12527614
- **Student 2:** Moncef Zakaria Belaid  K12455347

## 1. Introduction

During Phase I, our subgroup worked with Generative AI to investigate the behaviour of BiomedCLIP, a biomedical vision-language model, using radiological images.

Our project focuses on two main tasks: zero-shot image classification and text-to-image retrieval. We worked with the ROCOv2 and BoghdadyJR/radiology datasets.

Throughout this phase, we used ChatGPT and Claude.ai as supporting tools during the different stages of the project, from understanding the theoretical background to implementing and exploring our experiments.

## 2. How Generative AI Supported Our Work

One of our first challenges was understanding the project itself, including the model, the datasets, and the experimental objectives.

We used ChatGPT and Claude.ai to clarify the architecture of BiomedCLIP, understand the role of its image and text encoders, and learn how image and text embeddings are compared using similarity scores.

We also asked questions about the datasets to understand their structure and the differences between image captions, medical concepts, and modality labels.

During implementation, we used AI to explain unfamiliar Python code, answer technical questions, and help us understand errors and possible solutions.


## 3. Support During the Experiments

Our subgroup implemented two main experiments with BiomedCLIP.

The first experiment focused on zero-shot modality classification using ROCOv2. We evaluated the model on a balanced subset of 238 radiology images belonging to six modality classes. The notebook reported an accuracy of 91.6% and a macro-F1 score of 91.7%. We also investigated prompt sensitivity by comparing different text prompt formulations. The results showed that using full modality names increased accuracy to 96.2%, while a radiology-specific template achieved 95.4%.

The second experiment focused on text-to-image retrieval. We used a gallery of 1,000 validation images and evaluated 500 original captions as text queries. The notebook reported a Mean Reciprocal Rank of 0.717, a median rank of 1, and a mean rank of 5.6. We also investigated incorrect retrievals and examined whether the retrieved images had the same modality as the target images.

Generative AI supported our understanding of these experiments by explaining the concepts, helping us understand the implementation, and answering questions about evaluation metrics and code.

## 4. Benefits of Generative AI During Implementation

One particularly useful aspect was using our own pseudocode to describe the logic of an experiment and asking ChatGPT or Claude.ai to transform it into a more complete Python implementation.

The generated code could include additional functions, data-processing steps, evaluation procedures, and visualizations. This helped us explore more sophisticated implementations than our initial pseudocode.

However, we also needed to review the generated code, understand its structure, and test whether it correctly implemented our intended approach.

## 5. Limitations and Critical Evaluation

Our experiments also highlighted the importance of interpreting results carefully.

For example, the classification notebook showed that changing the wording of text prompts influenced the model's accuracy. This demonstrated that the choice of prompts is an important factor in zero-shot classification.

In the retrieval experiment, we also considered a possible limitation related to overlap between ROCOv2 and the PMC-15M pretraining data. This means that the retrieval results should not automatically be interpreted as performance on completely unseen images.

Generative AI helped us understand these issues and explore possible explanations, but the experimental outputs and limitations still needed to be examined critically.

## 6. Overall Reflection

Our experience showed that Generative AI can support both the learning and implementation stages of a machine-learning project.

It was useful for understanding BiomedCLIP, exploring the datasets, explaining unfamiliar Python code, and transforming pseudocode into more complete implementations.

At the same time, we learned that generated code can be unnecessarily complex and that AI-generated explanations and suggestions require verification.

Overall, we consider Generative AI a useful assistant during Phase I, but not a replacement for understanding the implementation, evaluating the experimental results, and making independent decisions.

