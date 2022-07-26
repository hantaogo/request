# request

do http request by a json config file.

## use

```shell
## do http request
## default config path: ./config.json
./request.exe ./config.json
```

```json
// config.json
{
	"url": "https://foo.bar/api", // api url
	"method": "post", // http method: get, post, put or delete, default: get
	"headers": { // headers
		"Content-Type": "application/json"
	},
  "params": { // url params: httos://foo.bar/api?pageNo=1&pageSize=10
    "pageNo": 1,
    "pageSize": 10
  },
  "data": { // body params: { name: "Jim Green", city: "New York" }
    "name": "Jim Green",
    "city": "New York"
  },
	"timeout": 10, // timeout default 10
	"encoding": "utf8", // encoding default utf8
	"pretty": true, // is print response pretty?, default false
	"log": "./foo.txt", // log file path
	"output": "./bar.json" // output file path
}
```


## lib
- [python3](https://www.python.org/)
- [requests](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
- [pyinstaller](https://pyinstaller.org/en/stable/)

## build windows exe
```shell
## build.bat
pyinstaller -F request.py
```