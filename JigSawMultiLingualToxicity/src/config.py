import transformers


MAX_LEN = 256
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = "../input/bert_base_multilingual_uncased/"
MODEL_PATH = "model.bin"
TOKENIZER = transformers.AutoTokenizer.from_pretrained(
    "bert-base-multilingual-uncased")
