#Servlet
##servlet部署
###使用web.xml 
```
<servlet>  
    <servlet-name>HelloWorld</servlet-name>  
    <servlet-class>HelloWorld</servlet-class>  
</servlet>  
  
<servlet-mapping>  
    <servlet-name>HelloWorld</servlet-name>  
    <url-pattern>/HelloWorld</url-pattern>  
</servlet-mapping>  
```
###使用@WebServlet
	@WebServlet("/HelloWorld")