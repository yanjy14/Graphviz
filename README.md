# Graphviz
Graphviz for Bio-CAD
##安装

```
	sudo apt-get install graphviz
```

##使用

	dot -T<type> -o<outfile> <infile.dot>
	输入文件是<infile.dot>，生成的格式由<type>指定，生成的文件是<outfile>。
	其中-T<type>包括：
	-Tps (PostScript),
	-Tsvg -Tsvgz (Structured Vector Graphics), 
	-Tfig (XFIG  graphics), 
	-Tmif  (FrameMaker graphics),
	-Thpgl (HP pen plotters),
	-Tpcl (Laserjet printers),
	-Tpng -Tgif (bitmap graphics),
	-Tdia (GTK+ based diagrams),
	-Timap (imagemap files for httpd servers for each node or edge  that  has a non-null "href" 	attribute.),
	-Tcmapx (client-side imagemap for use in html and xhtml).
##dot语言简介
1.digraph是有向图，graph是无向图，要注意，->用在有向图中，--用在无向图中表示一条边，不能混用。

```
digraph G {
	main -> parse -> execute;
}
```
2.常用属性