# Design Consideration in the game CancerGDV - CureIT

## Introduction
This code is a simple demonstration of 3-strategy evolution cancer tumor: 
glycoltyic cells (GLY), vascular overproducers (VOP), and defectors (DEF) proposed by Gluzman

This work is in progress, any contributions or issues are welcome on
GitHub at: https://github.com/sangttruong/cancergame

### Installation
Install and run the code as the following command

```console
git clone https://github.com/sangttruong/cancergame
```
### Gallery
We also provide a sample visualization from our code. Some demos:

![default-game](https://github.com/hieumtran/cancergame/blob/master/figures/default.png)
<div align="center">Initialize cancer game without user input</div>

![user-input](https://github.com/hieumtran/cancergame/blob/master/figures/user_input.png) 
<div align="center">Initialize cancer game with user input</div>

## Dependencies
* python (version>=3.7)
* numpy (version>=1.19.3)
* matplotlib (version>=3.3.0)

<!--
# Note:
* Adjust the game so that the user can make multiple choices for the game
* Decide on technique to choose the metric for the game - Most Difficult for now
* Changing dt can effect the game a lot. Especially in some cases, the game can automatically win without the affect of the users or lose or going on and on constantly
* Can do statistical analysis on the game without using AI to complete the paper in the mean time - This seems more possible direction for now
* Fix the game - current priority! - Temporarily fine
--> 

## Authors
This repository is currently maintained by Sang Truong, Hieu Tran, and Steven Borgaert. 

## Acknowledgements
We thank Andy Le, Brian Howard, Dee Wu for their initial work during Summer 2020.

## References
* Cancer treatment scheduling and dynamic heterogeneity in social dilemmas of tumour acidity and vasculature: https://pubmed.ncbi.nlm.nih.gov/28183139/
* Optimizing Cancer Treatment Using Game Theory: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6947530/
* Optimizing adaptive cancer therapy: dynamic programming and evolutionary game theory:  https://royalsocietypublishing.org/doi/pdf/10.1098/rspb.2019.2454
* egtplot: A Python Package for Three-Strategy Evolutionary Games: https://github.com/mirzaevinom/egtplot. Paper: https://www.biorxiv.org/content/10.1101/300004v2.full.pdf
* PDE numerical method: https://www.youtube.com/watch?v=ZSNl5crAvsw
* EAAI 2022 challenge: http://cs.gettysburg.edu/~tneller/games/aiagd/index.html
