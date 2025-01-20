#FROM gcr.io/distroless/java:11-nonroot
#FROM gcr.io/distroless/java:17-nonroot
FROM openjdk:21-jdk

COPY target/backend-*.jar /app/main.jar
WORKDIR /app
CMD ["java","-jar","main.jar"]
