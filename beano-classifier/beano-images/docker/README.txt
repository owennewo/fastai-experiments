docker build --build-arg MODEL_DIR=./model -t fastai-lesson2 .
docker run --rm --name fastai-lesson2 -p 8501:8501 -t fastai-lesson2