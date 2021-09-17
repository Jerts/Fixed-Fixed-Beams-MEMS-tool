# Fixed Fixed Beams MEMS tool
This project was created with the intention to offer an easy way to calculate the length of an array of fixed-fixed beams MEMS test structures. It consists of a very simple implementation through a GUI using PyQt5

Another of the intentions of publishing this project was to learn how software is released on GitHub.

## Usage

To calculate the length of the beams you should provide the thickness of the film, the Young Modulus of the material, the expected range of Residual Stress that you  want to detect, and also provide the number of beams you want to include in the array

The results indicate the length and the stress at which the beam is expected to buckle, these are provided on a table, with the option to save them on a CSV file

## Example

![example image](/img/example.png "Logo Title Text 1")

## Used equation

As described in [*Alvarez CRB, Aranda ML, Jacome AT, Arriaga WC. Test structures for residual stress monitoring in the integrated CMOS-MEMS process development*](https://ieeexplore.ieee.org/document/7520745) equation (3) is used.

![equation](/img/formula.png "Logo Title Text 1")

where *z* is the film thickness

## Music
The release plays:

Music: Evan King - [Fluoride-20XX]
https://www.youtube.com/channel/UCT1ZkP03V18LmOj8zbyP-Dw?
https://contextsensitive.bandcamp.com/