function refresh_task(){
    $.post('/interf_task', {'type': 'get_task', 'project': $('select#project').val()}, function(data){
        var l = data.task.length;
        $('table#task').find('tr.dam').remove();
        var tr = $('table#task').find('tr');
        if (l != 0){
            var html = '';
            for (i=0;i<l;i++){
                html += '<tr class="dam">';
                for (j=0;j<11;j++){
                    if (j==0){
                        html = html + '<td style="width:5%">'+(i+1)+'</td>';
                    }
                    else if (j==5){
                        if (data.task[i][j]==0){
                            html = html + '<td style="width:5%">未执行</td>';
                        }
                        else if (data.task[i][j]==1){
                            html = html + '<td style="width:5%">执行中</td>';
                        }
                        else if (data.task[i][j]==2){
                            html = html + '<td style="width:5%">已完成</td>';
                        }
                    }
                    else if (j==6){
                        var obj = parseInt((data.task[i][j]/data.task[i][7])*100);
                        if ((obj-data.task[i][9])==0){
                            html = html + '<td style="width:10%"><div class="progress progress-striped active"><div class="progress-bar" style="width: ' + obj + '%;">' + obj + '%' + '</div></div></td>'
                        }
                        else if ((obj-data.task[i][9])<=50){
                            html = html + '<td style="width:10%"><div class="progress progress-striped active"><div class="progress-bar progress-bar-warning" style="width: ' + obj + '%;">' + obj + '%' + '</div></div></td>'     
                        }
                        else {
                            html = html + '<td style="width:10%"><div class="progress progress-striped active"><div class="progress-bar progress-bar-danger" style="width: ' + obj + '%;">' + obj + '%' + '</div></div></td>'     
                        }
                    }
                    else if (j==10){
                        if (data.task[i][5]==1){
                            html += '<td style="width:20%"><button id="start" class="btn btn-success" disabled="disabled">启动</button>    '
                        }
                        else{
                            html += '<td style="width:20%"><button id="start" class="btn btn-success">启动</button>    '
                        };
                       html += '<button id="del" class="btn btn-danger">删除</button>    <button id="detail" type="submit" class="btn btn-primary">详情</button></td>'; 
                    }
                    else{
                        if (j==7 || j==8){
                            html = html + '<td style="width:5%">'+data.task[i][j]+'</td>';
                        }
                        else if(j==9){
                            html = html + '<td style="width:5%">'+data.task[i][j]+'%'+'</td>';
                        }
                        else if(j==4){
                            html = html + '<td style="width:15%">'+data.task[i][j]+'</td>';
                        }
                        else{
                            html = html + '<td style="width:10%">'+data.task[i][j]+'</td>';
                        };
                    };
                };
            };
            tr.after(html)
        };
    });
};


function tc(info, message){
    $("h4#myModalLabel").text(info);
    $("div.modal-body").text(message);
    $("button#send_alert").trigger("click"); 
};


$(function(){
    //建立webscoket，持续监听后台推送信息，刷新任务实时数据
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/task_i');
    socket.on('task_data', function(data) {
        if (data.msg=='ok'){
            refresh_task()
        };
    });

    //选择项目后，动态加载测试套
    $('select#project').change(function(){
        if ($(this).val() != 'none'){
            $.post('/suite', {'type': 'get_suite', 'project': $(this).val()}, function(data){
                var obj = $('select#suite');
                obj.empty();
                var html = '<option value="none">请选择测试套</option>';
                for (i=0;i<data.suite.length;i++){
                    html = html + '<option value="' + data.suite[i] + '">' + data.suite[i] + '</option>';
                };
                obj.html(html);
            });
            refresh_task()
        }
        else{
            $('select#suite').empty();
            $('select#suite').html('<option value="none">请选择测试套</option>');
            $('div#suite_data').hide();
        };
    });
    
    $('select#project').get(0).selectedIndex=1
    $("select#project").trigger("change"); 
    
    //新建任务
    $('button#new_task').on('click', function(){
        if ($('select#suite').val() == 'none'){
            tc('提示', "请先选择好测试套！")
            return
        };
        if ($('input#task_name').val() == ''){
            tc('提示', "任务名不能为空！")
            return
        };
        $.post('/interf_task', {'type': 'new_task', 'name': $('input#task_name').val(), 'project': $('select#project').val(), 'suite': $('select#suite').val()}, function(data){
            if (data.code == 200){
                refresh_task()
                tc('提示', "任务新建成功！")
                $('input#task_name').val('')
            }
            else{
                tc('提示', data.message)
            };
        
        });
    });
    
    //删除任务
    $('table#task').on('click', 'button#del', function(){
        var s = $(this).parents('tr').find('td').eq(5).text();
        if (s == '执行中'){
            tc('错误', '任务正在执行中，无法删除！')
            return
        };
        var name = $(this).parents('tr').find('td').eq(1).text();
        $.post('/interf_task', {'type': 'del_task', 'name': name, 'project': $('select#project').val()}, function(data){
            if (data.code==200){
                refresh_task()
                tc('提示', '任务删除成功！')
            }
            else{
                tc('提示', '任务删除失败！')
            };
        });
    });
    
    //启动任务
    $('table#task').on('click', 'button#start', function(){
        var name = $(this).parents('tr').find('td').eq(1).text();
        $.post('/interf_task', {'type': 'start_task', 'name': name, 'project': $('select#project').val()}, function(data){
            if (data.code == 200){
                refresh_task()
            }
            else{
                tc('提示', '任务启动失败')
            };
        });
    });
    
    //查看任务详情
    $('table#task').on('click', 'button#detail', function(){
        var name = $(this).parents('tr').find('td').eq(1).text();
        window.open('http://' + document.domain + ':' + location.port + '/task_detail?name='+name+'&project='+$('select#project').val());
    });
    
});