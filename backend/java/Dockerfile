FROM gcr.io/distroless/java:11-nonroot
COPY target/backend-*.jar /app/main.jar
WORKDIR /app
CMD ["main.jar"]
