# Cloud-Technologie und -Services

[AWS Dienste](https://aws.amazon.com/de/products/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc&awsf.re%3AInvent=*all&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)


## Bereitstellung und Betrieb der AWS-Cloud

Benutzer können die Ressourcen verwalten, bei der Benutzung aus drei Platformen.

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

![alt text](image-4.png)

Die VPC ist eine Netzwerk, die für die Verbindung vielzahle Geräts verfügbar ist.

![alt text](image-5.png)

*Virtual private gateway:* A virtual private gateway is the Amazon VPC side of a VPN connection. It acts as the
termination point for VPN connections.

*Customer gateway:* A customer gateway is the on-premises side of a VPN connection. It is a physical or
software appliance that is connected to your on-premises network and is responsible for establishing the VPN
connection to your VPC.

![alt text](image-6.png)

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-10.png)

![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)

>[!Note]
> The more loosely coupled the application components are, the better they will scale

>[!Note]
> A monolithic design refers to an architectural style where an application is built as a single, unified unit.
> 1. *Single Codebase:* All components of the application are part of one large codebase.
> 2. *Tightly Coupled:* Components are highly interdependent, making changes or scaling more challenging.
> 3. *Single Deployment:* The entire application is deployed as one unit, which can complicate updates and maintenance.
> 4. *Scalability Issues:* Scaling a monolithic application often requires scaling the entire application, rather than individual components.

![alt text](image-14.png)

![alt text](image-15.png)

An Availability Zone (AZ) is a component of the AWS global infrastructure that is made up of one or more discrete
data centers that have redundant power, networking, and connectivity. Each AZ is physically separated from Other
AZs within a region, and is designed to be fault-tolerant and provide low-latency networking.

![alt text](image-16.png)

![alt text](image-17.png)

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-21.png)


## Compute-Services

![alt text](image-24.png)

![alt text](image-25.png)

![alt text](image-27.png)

>[!Note]
> *AWS Auto Scaling* monitors your applications and automatically adjusts capacity to mantain steady, predictable performance at the lowest possible cost. Using AWS Auto Scaling, it's easy to setup application scaling for multiple resources across multiple services in minutes

>[!Note]
> Amazon Machine Images (AMIs): An AMI is a pre-configured virtual machine image that contains the operating system,
> application software, and any Other required components needed to launch an instance. AMIs can be used to create new
> instances in the same or a different region, which can be useful for disaster recovery purposes.

![alt text](image-28.png)

Um detalierte Informationen über *Kubernetes* zu erfahren, clicken Sie hierzu:

[Kubernets](https://kuberntes.io)

![alt text](image-29.png)

![alt text](image-30.png)

![alt text](image-32.png)

![alt text](image-33.png)

![alt text](image-34.png)

![alt text](image-35.png)

![alt text](image-37.png)

![alt text](image-38.png)


## Speicher-Services

![alt text](image-39.png)

![alt text](image-40.png)

![alt text](image-41.png)

![alt text](image-42.png)

![alt text](image-43.png)

![alt text](image-44.png)

![alt text](image-45.png)

![alt text](image-46.png)

![alt text](image-47.png)

![alt text](image-48.png)

[Speicherklassen](https://aws.amazon.com/de/s3/storage-classes/)

![alt text](image-49.png)

![alt text](image-50.png)

![alt text](image-51.png)

![alt text](image-52.png)

![alt text](image-53.png)

![alt text](image-54.png)

![alt text](image-55.png)

![alt text](image-56.png)

![alt text](image-58.png)

![alt text](image-59.png)

![alt text](image-60.png)

![alt text](image-61.png)

>[!Note]
> In the *AWS Marketplace* it's possible to:
> - Sell solutions to other AWS users
> - Buy third-party software that runs on AWS 

## Datenbank-Services

![alt text](image-62.png)

In-Memory-Datenbanken sind Datenbankmanagementsysteme, die den Arbeitsspeicher (RAM) eines Computers als primären Datenspeicher nutzen. Im Gegensatz zu herkömmlichen Datenbanken,
die Festplattenlaufwerke verwenden, speichern In-Memory-Datenbanken alle Daten im RAM, was zu deutlich schnelleren Zugriffszeiten und einer höheren Verarbeitungsgeschwindigkeit führt.

![alt text](image-63.png)

![alt text](image-64.png)

![alt text](image-65.png)

![alt text](image-74.png)

![alt text](image-66.png)

![alt text](image-67.png)

![alt text](image-68.png)

![alt text](image-70.png)

![alt text](image-71.png)

![alt text](image-72.png)


## Netzwerk-Services

![alt text](image-75.png)

A VPC can span all Availability Zones within an AWS Region.

>[!Note]
> *VPC peering* is useful for establishing a connection between 2 VPCs in different AWS regions

>[!Note]
> _AWS Transit Gateway_ acts as a highly scalable cloud router. It conects your Amazon Virtual Private Clouds (VPCs) and on-premises networks through a central hub.

![alt text](image-76.png)

![alt text](image-77.png)

A *Content Delivery Network (CDN)* is a system of geographically distributed servers that work together to deliver web content quickly and efficiently to users. Here are some key points about CDNs:

- *Speed and Performance:* CDNs cache content close to end users, reducing latency and improving load times for websites.
- *Reliability:* By distributing content across multiple servers, CDNs can handle high traffic volumes and mitigate the impact of hardware failures.
- *Cost Efficiency:* CDNs reduce bandwidth costs by caching content, which decreases the load on the origin server.
- *Security:* CDNs offer protection against Distributed Denial of Service (DDoS) attacks and other security threats.

Popular CDN providers include Akamai Technologies, Cloudflare, Amazon CloudFront, Fastly, and Google Cloud CDN.

![alt text](image-78.png)

![alt text](image-79.png)

![alt text](image-80.png)

![alt text](image-81.png)

![alt text](image-82.png)

![alt text](image-83.png)

![alt text](image-84.png)

![alt text](image-86.png)

![alt text](image-87.png)


## Kunstliche Intelligenz, Machine Learning und Analytic Services
### KI/ML-Services


![alt text](image-88.png)

![alt text](image-89.png)

![alt text](image-90.png)

### Datenanalyse-Services

![alt text](image-92.png)

![alt text](image-93.png)

![alt text](image-94.png)


## Verwaltungstools

![alt text](image-95.png)

![alt text](image-96.png)

![alt text](image-97.png)

![alt text](image-98.png)

![alt text](image-100.png)

![alt text](image-101.png)

AWS CloudTrail allows AWS customers to record API calls, sending log files to Amazon
S3 buckets for storage.

![alt text](image-102.png)

![alt text](image-103.png)

>[!Note]
>
> Serverless applications:
> - AWS Fargate
> - AWS Step Functions
> - Amazon DynamoDB
> - Amazon SNS

## Andere Services

![alt text](image-104.png)

![alt text](image-105.png)

![alt text](image-106.png)

![alt text](image-107.png)

*AWS software development kits (SDKs)* allow users to connect with and deploy AWS services
programmatically. AWS provides SDKs for several popular programming languages, including Java, Python,
JavaScript, and C++.

![alt text](image-108.png)

![alt text](image-109.png)

![alt text](image-110.png)

>[!Note]
>
> *AWS Service Catalog* allows organizations to create and manage catalogs of IT services that are approved
> for use on AWS. These IT services can include everything from virtual machine images, servers, software,
> and databases to complete multi-tier application architectures.
>
> *AWS Service Catalog* can limit employees' access to a portfolio of predefined AWS resources

>[!Note]
>
> _AWS IAM Access Analyzer_ helps to identify the resources in your organization and accounts, such as Amazon S3 buckets or IAM roles, shared with an external entity.
> This lets you identify unintended access to your resources and data, which is a security task.


## Zusammenfassung

![alt text](image-111.png)

![alt text](image-112.png)

![alt text](image-113.png)

![alt text](image-116.png)

![alt text](image-117.png)

![alt text](image-118.png)

![alt text](image-119.png)

![alt text](image-120.png)

![alt text](image-121.png)

![alt text](image-122.png)

![alt text](image-123.png)

![alt text](image-124.png)

![alt text](image-125.png)

![alt text](image-126.png)

![alt text](image-127.png)

![alt text](image-128.png)

![alt text](image-129.png)

![alt text](image-130.png)

![alt text](image-131.png)

![alt text](image-133.png)
