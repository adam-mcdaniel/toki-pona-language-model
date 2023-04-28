FROM ubuntu:latest

RUN apt update && \
    apt -y upgrade && \
    apt -y install python3 && \
    apt -y install python3-pip && \
    pip install numpy && \
    pip install pandas && \
    pip install matplotlib && \
    pip install seaborn && \
    pip install ipython && \
    pip install transformers && \
    pip install keras && \
    pip install gradio && \
    pip install mdtex2html

CMD ["bash"]
