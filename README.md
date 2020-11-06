# Predict Sao Paulo RealState values

[![author](https://img.shields.io/badge/Author-MarcelBittar-blue)](https://www.linkedin.com/in/marcelbittar/) [![](https://img.shields.io/badge/python-3.8.6+-blue.svg)](https://www.python.org/downloads/release/python-386/) [![](https://img.shields.io/badge/License-BSD%203--Clause-blue)](https://raw.githubusercontent.com/mabittar/imovsp/master/LICENSE) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/mabittar/imovsp/issues)

Deploy an app of Machine Learning aplication to predict values for Sao Paulo RealState 

> **Note:** This project is my first API deployment for Machine Learning model.

---

## The Data

The data was obtain from this [link](https://www.kaggle.com/argonalyst/sao-paulo-real-estate-sale-rent-april-2019) and all steps will be recorded on this repo.

---

## Steps:

- [x] **Setup environment**:

- VScode

- Python

- venv

- Flask

- Github

- [x] Generate Model (model.ipynb):

- import data
-  create model
-  compare metrics
-  export model


- [x] Create Api to get and post information (app.py)

- [x] Testing Api with Insomnia

![test with Insomnia](https://github.com/mabittar/imovsp/blob/master/imgs/test-post-json.JPG?raw=true)

- [x] Publish API online

APi was published to [https://imovsp.herokuapp.com/](https://imovsp.herokuapp.com/)

also a I made a new test with Insomnia with new values

![online test with Insomnia](https://github.com/mabittar/imovsp/blob/master/imgs/test-heroku.JPG?raw=true)

check all values used in [values_used.txt](https://github.com/mabittar/imovsp/blob/master/model/values_used.txt?raw=true)
---

## License

[BSD 3-Clause License](https://raw.githubusercontent.com/mabittar/imovsp/master/LICENSE)

---

## Porfolio
With you like it and want to see other projects please go to my portfolio at [mabittar.github.io](https://mabittar.github.io/)

## 

---
This exercise is part of Sigmoidal Course Data Science na Prática see more at [https://cursos.sigmoidal.ai/](https://cursos.sigmoidal.ai/)


![](https://github.com/carlosfab/escola-data-science/blob/master/img/novo_logo_bg_claro.png?raw=true)