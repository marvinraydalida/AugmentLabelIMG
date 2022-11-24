# AugmentLabelIMG 

Forked version of BendiXB/AugmentLabelIMG. Added new random augmentation such as blur, grayscale and adjustments to brightness and contrast.
This version can also work with JPEG files.

## Usage
0. Download the repository from the GitHub website and unzip it or directly clone it. 
`https://github.com/marvinraydalida/AugmentLabelIMG.git`
1. Clear the `dataset/` and `output/` directories of example data and copy your dataset to `dataset/` for it to be processed by the program.
2. Run `augment.py` in Python3. `sudo python3 augment.py`
3. Your dataset will now be augmented and saved to `output/`.

## Example
|rotation |random augment|not mirrored                      |mirrored                                            |
|---------|----------------------|----------------------------------|----------------------------------------------------|
|0°       |none                  |![0°](/output/sample-0.JPG)       |![0° mirrored](/output/sample-0-mirrored.JPG)       |
|90°      |none                  |![90°](/output/sample-90.JPG)     |![90° mirrored](/output/sample-90-mirrored.JPG)     |
|180°     |brightness + contrast |![180°](/output/sample-180.JPG)   |![180° mirrored](/output/sample-180-mirrored.JPG)   |
|270°     |grayscale             |![270°](/output/sample-270.JPG)   |![270° mirrored](/output/sample-270-mirrored.JPG)   |

## Contributers
@ockapunktnet
@BendiXB
@marvinraydalida