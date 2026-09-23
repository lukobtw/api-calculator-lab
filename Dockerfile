FROM python:3.11.16-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --upgrade --force-reinstall setuptools==84.0.0 wheel==0.48.0 \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip check

RUN python -c "import setuptools; print('SETUPTOOLS VERSION:', setuptools.__version__)" \
    && python -c "import wheel; print('WHEEL VERSION:', wheel.__version__)"

COPY app ./app

RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
