# Exercice 3, Section 1

This exercice is divided into two subsections that are as follows :

## Section 1.A

For this subsection of the exercice, you will be required to create a file called `docker-compose-A.yml` under
the [applications folder](../applications) that does the following :

1. Expose the `backend` application on the port `8082` of the host machine
2. Expose the `website` application on the port `80` of the host machine
3. Deploy the `qr` application in a private network
4. Create a shared volume between the `qr` application and the `website` that contains the generated QR codes. (:
   warning: The files generated by the `qr` application must not be committed to Git :exclamation:)
5. Load environment variables from `.env` files __THAT MUST NOT BE COMMITTED TO GIT__

## Section 1.B

For this subsection of the exercice, you will be required to create a file called `docker-compose-B.yml` under
the [applications folder](../applications) that does the following :

1. Inherit the configurations in `docker-compose-A.yml` (without duplicating them)
2. Deploy and configure a `minio` image inside `docker-compose` with persistent volume that allows it to serve as the
   local `s3`
3. Override the environment variables file of the `qr` in a way that allows it to store data inside an `s3`

## Turning in results

In order to run in the results of this exercice, you need to be able to provide the following files under their
appropriate paths (mentioned above) :

* `docker-compose-A.yml`
* `docker-compose-B.yml`

Additionally, you need to provide the following bash scripts under the [applications folder](../applications) that
contain the commands to launch the docker-compose projects :

* `launch-A.sh`
* `launch-B.sh`

:warning: Each subsection should be turned in separately. You will only work on a following subsection once all the
preceding subsection have been validated.