# Overview
In many image-to-image translation tasks, such as style transfer, object transfiguration, season transfer, and photo enhancement, acquiring perfectly aligned pairs of source and target images is often impractical. This project reimplements the solution proposed by Zhu et al., which leverages Cycle-Consistent Adversarial Networks (CycleGANs) to learn this translation in an unpaired setting.

# Features
- Unpaired Translation: Implementation focuses on learning a mapping from a source image domain X to a target domain Y without the need for paired examples.
- Adversarial and Cycle Consistency Loss: Utilized an adversarial loss to match the distribution of translated images with the target domain, and a cycle consistency loss to ensure that translating an image to the target domain and back to the source domain retains the original image content.

# Diverse Applications
The model showcases its versatility across various domains: it adeptly transforms standard images to emulate the distinctive style of emojis, providing a playful and creative angle to image translation. Additionally, the model has been trained on artworks by Monet, demonstrating its ability to infuse ordinary images with the impressionistic and vibrant qualities of Monet's paintings. Furthermore, the implementation includes a celebrity dataset, highlighting the model's effectiveness in capturing and translating the nuances of human facial features and expressions.

# Acknowledgements
This project is a reimplementation of the research by Jun-Yan Zhu, Taesung Park, Phillip Isola, and Alexei A. Efros. I acknowledge their groundbreaking work in the field of computer vision and deep learning.
