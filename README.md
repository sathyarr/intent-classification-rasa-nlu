# Intent Classification with Rasa-NLU
A simple Intent classification with Rasa NLU using tensorflow embedding and Of Course, Python

The given dataset(<b>NLP.csv</b>) contains data for 5 different intents.

The implementation goes through some pre-processing, training and testing sample data.

To Run:

Install the required packages with <b>requirements.txt</b>

To verify the installation of rasa_nlu, run these,

  <code>pip install rasa_nlu</code>

  <code>pip install rasa_nlu[tensorflow]</code>

Use the Jupyter notebook file

(or)

1. Keep all the files in same folder

2. Run the Python file(<b>process.py</b>) to pre-process and generate intermediate files

3. Train a Model using the command

<code>python -m rasa_nlu.train -c nlu_config.yml --data intentClassifiedFile.json -o models --fixed_model_name intentClassifier --project current --verbose</code>

4. Run <b>test.py</b> to test sample data

The code is tested and results are stored in <b>TestRun</b> folder for Reference

If you are more curious, <a href="https://rasa.com" target="_blank">Check out here</a>

Cheers!
