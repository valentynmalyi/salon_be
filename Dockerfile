FROM public.ecr.aws/lambda/python:3.10 as poetry-stage
ENV PYTHONUNBUFFERED=1
WORKDIR ${LAMBDA_TASK_ROOT}
RUN pip install --upgrade pip
RUN pip install poetry

################

FROM poetry-stage as requirements-stage
COPY ./pyproject.toml ./poetry.lock* ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir -r requirements.txt

################

FROM requirements-stage
COPY . .
