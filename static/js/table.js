$(document).ready(function(){
    $('#datatable').DataTable({
        "bPaginate": true, //翻页功能
        "bLengthChange": true, //改变每页显示数据数量
        "bFilter": true, //过滤功能
        "bSort": false, //排序功能
        "bInfo": true,//页脚信息
        "bAutoWidth": true,//自动宽度
        "sPaginationType": "full_numbers",
		"bScrollAutoCss": true,
		"oLanguage": {
			 "sLengthMenu": "显示 _MENU_ 条",
			 "sZeroRecords": "抱歉， 没有找到",
			 "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
			 "sInfoEmpty": "没有数据",
			 "sInfoFiltered": "(从 _MAX_ 条数据中检索)",
			 "oPaginate": {
			 "sFirst": "首页",
			 "sPrevious": "前一页",
			 "sNext": "后一页",
			 "sLast": "尾页"
			},
			 "sSearch":"搜索"
		}
 
        });});
 
