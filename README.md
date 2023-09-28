# Hinglish Generator

## Training
This repository consists of the code that was used to make the hinglish generator by finetuning the T5-base transformer model. Since there was no dataset in the style of hinglish requested I had to resort to a hinglish datasets with just in english. 

T5 - base transformer was fine-tuned on the selected dataset with around 189k rows in the training dataset and about 2k testing rows from validation set from huggingface. The fine tuning was carried out on kaggle with the help of 2 Nvidia t4 gpus which possess decent processing power.The model ran around 10 epocs with a bleu score of 5 which is decent for the number of epochs. 

## Limitations
Due to the constraints posed by kaggle which is the fact that its gpus cant be used for more than 12 hours straight the model only ran 10 epochs. The model can be improved vastly and has the capacity to better if provided with more time and  resoruces.
Finally after training for about 11 hours the model was saved and uploaded on huggingface for usage and reference, but it can only generate hinglish that isnt in the hindi script. To further achieve what was tasked tools such as nltk and googletrans libraries were used to achieve the end goal.

Please do understand that the model can be built better if more time and processing power. The model has also been hosted on streamlit for ease of access and its link is given below. 

The reason behind my choice of T5 is its ability of T5 to perform multiple NLP tasks by simply changing the prefix of the input is a significant advantage. Additionally, its performance on various tasks has made it one of the most promising approaches for NLP applications. As the model is pre-trained on a mixture of unsupervised and supervised tasks, it has the potential to generalize well to new tasks.

## Links:

Streamlit : https://hinglish-generator.streamlit.app/
Huggingface model : VasRosa/Hinglish-finetuned

## PS : Please wait for about a minute and retry the streamlit app as the model has to be loaded on huggingface as an api of the model i have uploaded is being used
## PS : All the above links are my work and arent copied links of someone elses work. Can reach out for clarification
