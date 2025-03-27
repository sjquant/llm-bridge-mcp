# Use UV's official Python 3.11 Alpine image which comes with UV pre-installed
FROM ghcr.io/astral-sh/uv:python3.11-alpine

# Install build dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Set the working directory
WORKDIR /app

# Use system python without virtual environment
ENV UV_PROJECT_ENVIRONMENT=/usr/local

# Install dependencies first (without the project)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Copy the project into the image
COPY . .

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

CMD ["llm-bridge-mcp"]