const options = {
    key: 'smHKrns7WTdxqtn8SLSWkKRezjQIwsGn', // REPLACE WITH YOUR KEY !!!
    lat: -16.6,
    lon: -64.3,
    zoom: 6,
};

windyInit(options, windyAPI => {
    const { store, picker, broadcast, overlays } = windyAPI;

    //picker.on('pickerOpened', latLon => {
    //// picker has been opened at latLon coords
    //    console.log(latLon);
//
    //    const { lat, lon, values, overlay } = picker.getParams();
    //    // -> 48.4, 14.3, [ U,V, ], 'wind'
    //    console.log(lat, lon, values, overlay);
//
    //    const windObject = utils.wind2obj(values);
    //    console.log(windObject);
    //});

//tipo
    store.set('overlay', 'wind');

//picker position
    picker.on('pickerMoved', latLon => {
        // picker was dragged by user to latLon coords
        console.log(latLon);
    });
	
    // Wait since wather is rendered
    broadcast.once('redrawFinished', () => {
        picker.open({ lat: -17.4, lon: -64.3 });
        // Opening of a picker (async)
    });

//metrica
    //const windMetric = overlays.wind.metric;
    console.log(overlays.wind.listMetrics());
    // ['kt', 'bft', 'm/s', 'km/h', 'mph'] .. available metrics

    overlays.wind.setMetric('kt');
    // Metric for wind was changed to bft

    broadcast.on('metricChanged', (overlay, newMetric) => {
        // Any changes of any metric can be observed here
        console.log(overlay, newMetric);
    });

//popup
//const { map } = windyAPI;
//L.popup()
//        .setLatLng([-16.7901535, -65.5886536])
//        .setContent('TEMPERATURA')
//        .openOn(map);


});
