ymaps.ready(init);

function init() {
    var map = new ymaps.Map('map', {
        center: [60.03335995244681,30.65346289881127],
        zoom: 16,
        controls: ['zoomControl'],
        behaviors: ['drag']
    });

    var placemark = new ymaps.Placemark([60.03335995244681,30.65346289881127], {
                hintContent: '<div class="map__hint">Маникюр и педикюр +79216428642</div>',
                balloonContent: [
                    '<div class="map__balloon">',
                    '<img class="map__img" src="./static/images/map/logo.svg" alt="Мастер ногтевого сервиса во Всеволожске"/>',
                    'Мастер ногтевого сервиса во Всеволожске, маникюр и педикюр. Адрес: г.Всеволожск, Шевченко 18/2',
                    '</div>'
                ].join('')
            },
            {
                iconLayout: 'default#image',
                iconImageHref: './static/images/map/marker.svg',
                iconImageSize: [50, 70],
                iconImageOffset: [-30, -70],
            });
    
    map.geoObjects.add(placemark);
    
}