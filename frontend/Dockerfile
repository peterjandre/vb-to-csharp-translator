FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install only production dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application code
COPY . .

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