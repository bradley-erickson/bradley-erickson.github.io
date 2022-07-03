html:
	export DEBUG=False && cd src && python3 app.py &
	sleep 10
	wget -r http://127.0.0.1:8050/
	wget -r http://127.0.0.1:8050/_dash-layout
	wget -r http://127.0.0.1:8050/_dash-dependencies
	mv 127.0.0.1+8050 build
	sed -i 's/_dash-layout/_dash-layout.json/g' build/_dash-component-suites/dash/dash-renderer/build/*.js
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' build/_dash-component-suites/dash/dash-renderer/build/*.js
	mv build/_dash-layout build/_dash-layout.json	
	mv build/_dash-dependencies build/_dash-dependencies.json
	ps | grep python | awk '{print $$1}' | xargs kill -9

clean:
	rm -rf build/
	ps | grep python | awk '{print $$1}' | xargs kill -9
