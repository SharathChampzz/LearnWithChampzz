<h2><a href="https://leetcode.com/problems/string-to-integer-atoi/">8. String to Integer (atoi)</a></h2><h3>Medium</h3><hr><div element-id="1192"><p element-id="1191">Implement the <code element-id="1190">myAtoi(string s)</code> function, which converts a string to a 32-bit signed integer (similar to C/C++'s <code element-id="1189">atoi</code> function).</p>

<p element-id="1188">The algorithm for <code element-id="1187">myAtoi(string s)</code> is as follows:</p>

<ol element-id="1186">
	<li element-id="1185">Read in and ignore any leading whitespace.</li>
	<li element-id="1184">Check if the next character (if not already at the end of the string) is <code element-id="1183">'-'</code> or <code element-id="1182">'+'</code>. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.</li>
	<li element-id="1181">Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.</li>
	<li element-id="1180">Convert these digits into an integer (i.e. <code element-id="1179">"123" -&gt; 123</code>, <code element-id="1178">"0032" -&gt; 32</code>). If no digits were read, then the integer is <code element-id="1177">0</code>. Change the sign as necessary (from step 2).</li>
	<li element-id="1176">If the integer is out of the 32-bit signed integer range <code element-id="1175">[-2<sup element-id="1174">31</sup>, 2<sup element-id="1173">31</sup> - 1]</code>, then clamp the integer so that it remains in the range. Specifically, integers less than <code element-id="1172">-2<sup element-id="1171">31</sup></code> should be clamped to <code element-id="1170">-2<sup element-id="1169">31</sup></code>, and integers greater than <code element-id="1168">2<sup element-id="1167">31</sup> - 1</code> should be clamped to <code element-id="1166">2<sup element-id="1165">31</sup> - 1</code>.</li>
	<li element-id="1164">Return the integer as the final result.</li>
</ol>

<p element-id="1163"><strong element-id="1162">Note:</strong></p>

<ul element-id="1161">
	<li element-id="1160">Only the space character <code element-id="1159">' '</code> is considered a whitespace character.</li>
	<li element-id="1158"><strong element-id="1157">Do not ignore</strong> any characters other than the leading whitespace or the rest of the string after the digits.</li>
</ul>

<p element-id="1156">&nbsp;</p>
<p element-id="1155"><strong class="example" element-id="1154">Example 1:</strong></p>

<pre element-id="1153"><strong element-id="1152">Input:</strong> s = "42"
<strong element-id="1151">Output:</strong> 42
<strong element-id="1150">Explanation:</strong> The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u element-id="1149">42</u>" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-2<sup element-id="1148">31</sup>, 2<sup element-id="1147">31</sup> - 1], the final result is 42.
</pre>

<p element-id="1146"><strong class="example" element-id="1145">Example 2:</strong></p>

<pre element-id="1144"><strong element-id="1143">Input:</strong> s = "   -42"
<strong element-id="1142">Output:</strong> -42
<strong element-id="1141">Explanation:</strong>
Step 1: "<u element-id="1140">   </u>-42" (leading whitespace is read and ignored)
            ^
Step 2: "   <u element-id="1139">-</u>42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -<u element-id="1138">42</u>" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-2<sup element-id="1137">31</sup>, 2<sup element-id="1136">31</sup> - 1], the final result is -42.
</pre>

<p element-id="1135"><strong class="example" element-id="1134">Example 3:</strong></p>

<pre element-id="1133"><strong element-id="1132">Input:</strong> s = "4193 with words"
<strong element-id="1131">Output:</strong> 4193
<strong element-id="1130">Explanation:</strong>
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u element-id="1129">4193</u> with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-2<sup element-id="1128">31</sup>, 2<sup element-id="1127">31</sup> - 1], the final result is 4193.
</pre>

<p element-id="1126">&nbsp;</p>
<p element-id="1125"><strong element-id="1124">Constraints:</strong></p>

<ul element-id="1123">
	<li element-id="1122"><code element-id="1121">0 &lt;= s.length &lt;= 200</code></li>
	<li element-id="1120"><code element-id="1119">s</code> consists of English letters (lower-case and upper-case), digits (<code element-id="1118">0-9</code>), <code element-id="1117">' '</code>, <code element-id="1116">'+'</code>, <code element-id="1115">'-'</code>, and <code element-id="1114">'.'</code>.</li>
</ul>
</div>