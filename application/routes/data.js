/**
 * @swagger
 * tags:
 *   name: Data
 *   description: Data management APIs
 */

/**
 * @swagger
 * /data:
 *   get:
 *     summary: Retrieve data for a specific device
 *     tags: [Data]
 *     parameters:
 *       - name: deviceId
 *         in: query
 *         required: true
 *         description: The ID of the device
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Device data retrieved
 *       404:
 *         description: Device not found
 *       500:
 *         description: Server error
 */
app.get('/data', (req, res) => {
  // Logic to retrieve device data
});

/**
 * @swagger
 * /data:
 *   post:
 *     summary: Submit data for a specific device
 *     tags: [Data]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               deviceId:
 *                 type: string
 *               value:
 *                 type: number
 *     responses:
 *       201:
 *         description: Data submitted
 *       400:
 *         description: Invalid input
 *       500:
 *         description: Server error
 */
app.post('/data', (req, res) => {
  // Logic to submit device data
});
