FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install all dependencies (needed for build)
RUN npm ci && npm cache clean --force

# Copy application code
COPY . .

# Accept build argument and set as environment variable
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}

# Build the application
RUN npm run build

# Remove unnecessary files
RUN rm -rf node_modules/.cache && \
    rm -rf .next/cache && \
    npm prune --production

# Expose port
EXPOSE 3000

ENV NODE_ENV=production

# Start the application
CMD ["npm", "start"] 