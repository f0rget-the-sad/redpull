# redpull

Download all attachments for Redmine issue.

## Requrenments

* python >= 3.6
* [redminelib](https://github.com/maxtepkeev/python-redmine)
```sh
	pip install python-redmine
```
* Redmine API access key
```
	The API key can be found on users account page when logged in,  on the right-hand pane of the default layout.
```

## Usage

```sh
./redpull 24680
Connecting to: https://redmine.interfacemasters.com/redmine
Hi, Stranger
Issue #24680 Something not work
Attachments: ['attachment1.tar', 'packets.pcap', 'logs.xz']
Start downloading...
	* attachment1.tar
	* packets.pcap
	* logs.xz
Successfully downloaded 3 attachments to /tmp/24680/
```

## TODO

[] Error handling
