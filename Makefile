html:
	export DEBUG=False && cd src && python3 app.py &
	sleep 30
	wget -r http://127.0.0.1:8050/
	wget -r http://127.0.0.1:8050/_dash-layout
	wget -r http://127.0.0.1:8050/_dash-dependencies
	ls -al 127.0.0.1:8050/_dash-component-suites
	sed -i 's/_dash-layout/_dash-layout.json/g' 127.0.0.1:8050/_dash-component-suites/dash/*.js
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' 127.0.0.1:8050/_dash-component-suites/dash/*.js
	mv 127.0.0.1:8050/_dash-layout 127.0.0.1:8050/_dash-layout.json	
	mv 127.0.0.1:8050/_dash-dependencies 127.0.0.1:8050/_dash-dependencies.json
	cp _static/async* 127.0.0.1:8050/_dash-component-suites/dash_core_components/
	ps | grep python | awk '{print $$1}' | xargs kill -9

clean:
	rm -rf 127.0.0.1:8050/
