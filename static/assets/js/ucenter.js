
//user/update
$("#user-update").submit(function () {
    var _this = $(this)
    $.post(_this.data('action'), _this.serializeArray()).done(function (data) {
        if (data) {
            _this.find('.import').html('')
            $.each(data, function (index, item) {
                _this.find('#' + index).parents('.form-group').find('.import').html(item.join('、'))
            })
        }
    });
    return false
});

//user/login
$("#user-login").submit(function () {
    var _this = $(this)
    $.post(_this.data('action'), _this.serializeArray()).done(function (data) {
        if (data) {
            importState('.import', data.state)
            _this.find('.import .import-msg').html(data.msg)
            if (data.state == 1){
                locationUrl('.import .import-second', 5000, data.url)
            }
        }
    });
    return false
});

function importState(importClass, state) {
    if (state == 1)
        $(importClass).removeClass('import-error').addClass('import-success')
    else if (state == 0)
        $(importClass).removeClass('import-success').addClass('import-error')
}

function locationUrl(importClass, second, url) {
    setTimeout(function () {
        location.href = url
    }, second+1000)
    setInterval(function () {
        $(importClass).html('<a href="'+url+'" title="点击跳转">'+(second/1000)+' 秒后跳转'+'</a>')
        second-=1000
    },1000)
}

