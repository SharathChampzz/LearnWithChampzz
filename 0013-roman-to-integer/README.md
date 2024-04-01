<h2><a href="https://leetcode.com/problems/roman-to-integer/">13. Roman to Integer</a></h2><h3>Easy</h3><hr><div element-id="1054"><p element-id="1053">Roman numerals are represented by seven different symbols:&nbsp;<code element-id="1052">I</code>, <code element-id="1051">V</code>, <code element-id="1050">X</code>, <code element-id="1049">L</code>, <code element-id="1048">C</code>, <code element-id="1047">D</code> and <code element-id="1046">M</code>.</p>

<pre element-id="1045"><strong element-id="1044">Symbol</strong>       <strong element-id="1043">Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p element-id="1042">For example,&nbsp;<code element-id="1041">2</code> is written as <code element-id="1040">II</code>&nbsp;in Roman numeral, just two ones added together. <code element-id="1039">12</code> is written as&nbsp;<code element-id="1038">XII</code>, which is simply <code element-id="1037">X + II</code>. The number <code element-id="1036">27</code> is written as <code element-id="1035">XXVII</code>, which is <code element-id="1034">XX + V + II</code>.</p>

<p element-id="1033">Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code element-id="1032">IIII</code>. Instead, the number four is written as <code element-id="1031">IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code element-id="1030">IX</code>. There are six instances where subtraction is used:</p>

<ul element-id="1029">
	<li element-id="1028"><code element-id="1027">I</code> can be placed before <code element-id="1026">V</code> (5) and <code element-id="1025">X</code> (10) to make 4 and 9.&nbsp;</li>
	<li element-id="1024"><code element-id="1023">X</code> can be placed before <code element-id="1022">L</code> (50) and <code element-id="1021">C</code> (100) to make 40 and 90.&nbsp;</li>
	<li element-id="1020"><code element-id="1019">C</code> can be placed before <code element-id="1018">D</code> (500) and <code element-id="1017">M</code> (1000) to make 400 and 900.</li>
</ul>

<p element-id="1016">Given a roman numeral, convert it to an integer.</p>

<p element-id="1015">&nbsp;</p>
<p element-id="1014"><strong class="example" element-id="1013">Example 1:</strong></p>

<pre element-id="1012"><strong element-id="1011">Input:</strong> s = "III"
<strong element-id="1010">Output:</strong> 3
<strong element-id="1009">Explanation:</strong> III = 3.
</pre>

<p element-id="1008"><strong class="example" element-id="1007">Example 2:</strong></p>

<pre element-id="1006"><strong element-id="1005">Input:</strong> s = "LVIII"
<strong element-id="1004">Output:</strong> 58
<strong element-id="1003">Explanation:</strong> L = 50, V= 5, III = 3.
</pre>

<p element-id="1002"><strong class="example" element-id="1001">Example 3:</strong></p>

<pre element-id="1000"><strong element-id="999">Input:</strong> s = "MCMXCIV"
<strong element-id="998">Output:</strong> 1994
<strong element-id="997">Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p element-id="996">&nbsp;</p>
<p element-id="995"><strong element-id="994">Constraints:</strong></p>

<ul element-id="993">
	<li element-id="992"><code element-id="991">1 &lt;= s.length &lt;= 15</code></li>
	<li element-id="990"><code element-id="989">s</code> contains only&nbsp;the characters <code element-id="988">('I', 'V', 'X', 'L', 'C', 'D', 'M')</code>.</li>
	<li element-id="987">It is <strong element-id="986">guaranteed</strong>&nbsp;that <code element-id="985">s</code> is a valid roman numeral in the range <code element-id="984">[1, 3999]</code>.</li>
</ul>
</div>