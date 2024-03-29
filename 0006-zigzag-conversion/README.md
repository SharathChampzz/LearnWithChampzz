<h2><a href="https://leetcode.com/problems/zigzag-conversion/">6. Zigzag Conversion</a></h2><h3>Medium</h3><hr><div element-id="644"><p element-id="643">The string <code element-id="642">"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre element-id="641">P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p element-id="640">And then read line by line: <code element-id="639">"PAHNAPLSIIGYIR"</code></p>

<p element-id="638">Write the code that will take a string and make this conversion given a number of rows:</p>

<pre element-id="637">string convert(string s, int numRows);
</pre>

<p element-id="636">&nbsp;</p>
<p element-id="635"><strong class="example" element-id="634">Example 1:</strong></p>

<pre element-id="633"><strong element-id="632">Input:</strong> s = "PAYPALISHIRING", numRows = 3
<strong element-id="631">Output:</strong> "PAHNAPLSIIGYIR"
</pre>

<p element-id="630"><strong class="example" element-id="629">Example 2:</strong></p>

<pre element-id="628"><strong element-id="627">Input:</strong> s = "PAYPALISHIRING", numRows = 4
<strong element-id="626">Output:</strong> "PINALSIGYAHRPI"
<strong element-id="625">Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p element-id="624"><strong class="example" element-id="623">Example 3:</strong></p>

<pre element-id="622"><strong element-id="621">Input:</strong> s = "A", numRows = 1
<strong element-id="620">Output:</strong> "A"
</pre>

<p element-id="619">&nbsp;</p>
<p element-id="618"><strong element-id="617">Constraints:</strong></p>

<ul element-id="616">
	<li element-id="615"><code element-id="614">1 &lt;= s.length &lt;= 1000</code></li>
	<li element-id="613"><code element-id="612">s</code> consists of English letters (lower-case and upper-case), <code element-id="611">','</code> and <code element-id="610">'.'</code>.</li>
	<li element-id="609"><code element-id="608">1 &lt;= numRows &lt;= 1000</code></li>
</ul>
</div>