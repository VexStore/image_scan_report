## WTF is This ?

This is a collection of container vulnerability scans of top official docker images using different vulnerability scanners like snyk, gryper and trivy.

The idea is to drive home the point that discrepancies between each scanner. Next step is to understand why these arise. 

## How To Run ? 

### Prerequisites

Behind the scenes this script uses [vimp](https://github.com/mchmarny/vimp). So make sure it is installed, [see the installation guide](https://github.com/mchmarny/vimp#installation)

The scanners need to be installed too.

[Installing Snyk](https://docs.snyk.io/snyk-cli/install-or-update-the-snyk-cli)
[Installing Trivy](https://github.com/aquasecurity/trivy#quick-start)
[Installing Grype](https://github.com/anchore/grype#installation)

Simply run the command:

```
python main.py
```

This is will start the scanning process for all the images specified in main.py. You can edit it to change the images you want to scan.

The raw scans of each tool would be saved in their respective directories eg `./grype`, `./snyk` etc

You can find the vimp sqlite DB at `~/.vimp.db` . 