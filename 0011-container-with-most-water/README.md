<h2><a href="https://leetcode.com/problems/container-with-most-water/">11. Container With Most Water</a></h2><h3>Medium</h3><hr><div element-id="1070"><p element-id="1069">You are given an integer array <code element-id="1068">height</code> of length <code element-id="1067">n</code>. There are <code element-id="1066">n</code> vertical lines drawn such that the two endpoints of the <code element-id="1065">i<sup element-id="1064">th</sup></code> line are <code element-id="1063">(i, 0)</code> and <code element-id="1062">(i, height[i])</code>.</p>

<p element-id="1061">Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p element-id="1060">Return <em element-id="1059">the maximum amount of water a container can store</em>.</p>

<p element-id="1058"><strong element-id="1057">Notice</strong> that you may not slant the container.</p>

<p element-id="1056">&nbsp;</p>
<p element-id="1055"><strong class="example" element-id="1054">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" element-id="1053">
<pre element-id="1052"><strong element-id="1051">Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong element-id="1050">Output:</strong> 49
<strong element-id="1049">Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p element-id="1048"><strong class="example" element-id="1047">Example 2:</strong></p>

<pre element-id="1046"><strong element-id="1045">Input:</strong> height = [1,1]
<strong element-id="1044">Output:</strong> 1
</pre>

<p element-id="1043">&nbsp;</p>
<p element-id="1042"><strong element-id="1041">Constraints:</strong></p>

<ul element-id="1040">
	<li element-id="1039"><code element-id="1038">n == height.length</code></li>
	<li element-id="1037"><code element-id="1036">2 &lt;= n &lt;= 10<sup element-id="1035">5</sup></code></li>
	<li element-id="1034"><code element-id="1033">0 &lt;= height[i] &lt;= 10<sup element-id="1032">4</sup></code></li>
</ul>
</div>