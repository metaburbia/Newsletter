<html>
<head><title></title></head>
<body>


</body>
</html>
<html>
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>US Holiday 2011</title>

   <style>

   body, html {
   	font-family : Verdana, Arial, Helvetica, sans-serif;
   	font-size : 10pt;
   }
   
   td, th {
   font-size : 9pt;
   }
   
	a {
		text-decoration : none;
		color : #000000;
		
	}
  	a:hover {
		text-decoration : underline;
		color : #000000;
		
	}
td.mainbar h2 {
	font-family: Georgia;
	font-size: 18px;
	font-weight: normal;
	color: #000000;
	margin: 20px 0 8px 0;
	padding: 0;
}

td.mainbar h2 a {
	font-family: Georgia;
	font-size: 18px;
	font-weight: normal;
	color: #000000;
	text-decoration: none;
}   
   

table.sidebar h3 {
	font-family: Georgia;
	font-size: 18px;
	font-weight: normal;
	color: #000000;
	margin: 0 0 10px 0;
	padding: 0;
}

table.sidebar p {
	font-family: Georgia;
	font-size: 12px;
	font-weight: normal;
	color: #000000;
	margin: 0 0 12px 0;
	padding: 0;
}

table.sidebar p.miniheader {
	font-family: Georgia;
	font-size: 12px;
	font-weight: bold;
	color: #000000;
	margin: 0 0 4px 0;
	padding: 0;
}   
   .clearfix {
   	display: inline-block;
   }
   
   img {border:none;}
   .clearfix:after {
	clear: both;
	content: '.';
	display: block;
	visibility: hidden;
	height: 0;
}

   .narr {
   	font-size : 1.4em;
   }
   #narrh {
   	font-size : 2.0em;
   }	
   #tbw * {
   	font-size : 0.92em;
   }
    #tbw td.cond {
   	font-style : italic;

   }
     #tbw td.temp {
   		padding-left : 4px;

   }
   #newsm * dd {
   	margin-left:0px;
   	padding-left : 0px;
   }
    #newsm * dt {
   	margin-top:1em;
   	font-weight:bold;

   }
   </style>
</head>
<body>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td align="center" valign="top">
         
         <table width="668" border="0" cellspacing="0" cellpadding="0">
            <tr>
               <td valign="top">
                  
                  <table width="668" border="0" cellspacing="20" cellpadding="0">
                     <tr>
                     <td >
                         <h2>Hols are getting closer</h2>
                         <p style="font-size:1.6em;">

                         
                                                     <img align="middle"   style="display: inline; float:left; margin-right : 8px;"  src="cid:image1" />
                         
<?php include('intro.inc');?>					
                           </p>                                                
                     </td><td valign="bottom"><h4 class="meta">Exchange Rate</h4> 
                     <p><?php include('currency.inc');?></p>   
                     
                     </td>
                     </tr>
                     <tr>
                        <td width="336" align="left" valign="top" class="mainbar">
							<?php include('narrative.inc');?>
                           
							<!-- 
							<img src="http://development.cloudsoup.com/holiday/htdocs/img/pics/216309929_dd7d58425c.jpg" />
                            -->
<div id="newsm">
                           <h2>And Elsewhere?</h2>
                         
<?php 
include('weatherTable.inc');
?>     		
 				
     					
     						<h2>News from round and about</h2>
   
     			
     			     					<?php include('newsfeeds.inc');?>                        
 </div>			
     						</td>                        
                        <td width="240" valign="top">
                          
                           <table width="240" border="0" cellspacing="0" cellpadding="0" class="sidebar">
                              <tr>
                                 <td>
									                              </td>
                              </tr>

                              <tr>
                                 <td>
                                 	<h4 class="meta">Some photos for your delight</h4>

                                 <?php include('flickr.inc');?>
                                 </td>
                              </tr>

                           </table>
                           
                        </td>
                     </tr>
                  </table>
                  
               </td>
            </tr>
         </table>
         
      </td>
   </tr>
</table>

</body>
</html>