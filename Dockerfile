# Dockerfile for Nginx serving Vite app

# Step 1: Build the Vite app
FROM oven/bun:latest AS build

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN bun install

# Copy the source code
COPY . .

# Build the Vite app
RUN bun run build

# Step 2: Use Nginx to serve the built files
FROM nginx:latest

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx/nginx.conf /etc/nginx/conf.d/

# Copy the built Vite app files to Nginx's html directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
