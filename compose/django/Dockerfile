# More Datascience frendly gist can be found here: https://gist.github.com/ruddra/870d7a51238ddfa4b50375086c12a4f5
# pull official python alpine image
FROM python:3.8

# Set Environment Variable
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

# Making source and static directory
RUN mkdir /src
RUN mkdir /static

# Creating Work Directory
WORKDIR /src

# Adding mandatory packages to docker
RUN pip install --upgrade cython
RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get install -y libgl1

RUN apt-get install -y build-essential libzbar-dev

RUN apt-get install -y gettext

#RUN apt-get install postgresql

# un-comment if you want to install numpy, pandas, scipy etc and their supported dependencies
# RUN pip install --no-cache-dir matplotlib pandas

# un-comment if you use multiples languages
# RUN ln -s /usr/include/locale.h /usr/include/xlocale.h


# Installing requirements.pip from project
COPY ./src/requirements.pip /scripts/
RUN pip install --no-cache-dir -r /scripts/requirements.pip


# removing temporary packages from docker and removing cache 
RUN find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

# CMD will run when this dockerfile is running
CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; gunicorn src_config.wsgi -b 0.0.0.0:8000 --reload & celery --app myapp.tasks worker --loglevel=INFO"]
