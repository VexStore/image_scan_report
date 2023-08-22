images = [
    "alpine",
    "nginx",
    "busybox",
    "ubuntu",
    "python",
    "redis",
    "postgres",
    "node",
    "httpd",
    "mongo",
    "memcached",
    "mysql",
    "traefik",
    "mariadb",
    "docker",
    "rabbitmq",
    "openjdk",
    "golang",
    "registry",
    "wordpress",
    "centos",
    "debian",
    "php",
    "hashicorp/consul",
    "influxdb",
    "nextcloud",
    "sonarqube",
    "haproxy",
    "ruby",
    "amazonlinux",
    "tomcat",
    "maven",
    "eclipse-mosquitto",
    "telegraf",
    "caddy",
    "bash",
    "adminer",
    "ghost",
    "kong",
    "zookeeper",
    "neo4j",
    "perl",
    "buildpack-deps",
    "mongo-express",
    "gradle",
    "cassandra",
    "logstash",
]

import os
import subprocess


# Create folders if they don't exist
for folder_name in ["trivy", "snyk", "grype"]:
    os.makedirs(folder_name, exist_ok=True)

# Iterate through images
for image in images:
    print(f"Processing image: {image}")

    # Run vimp import command
    vimp_command = f"vimp import --source {image}"
    subprocess.run(vimp_command, shell=True, check=True)

    image = image.replace("/", "_")
    # Move snyk result
    snyk_mv_command = f"cp /tmp/snyk* ./snyk/snyk-{image}.json && rm /tmp/snyk*"
    subprocess.run(snyk_mv_command, shell=True, check=True)

    # Move trivy result
    trivy_mv_command = f"cp /tmp/trivy* ./trivy/trivy-{image}.json && rm /tmp/trivy*"
    subprocess.run(trivy_mv_command, shell=True, check=True)

    # Move grype result
    grype_mv_command = f"cp /tmp/grype* ./grype/grype-{image}.json && rm /tmp/grype*"
    subprocess.run(grype_mv_command, shell=True, check=True)

print("Processing complete.")
