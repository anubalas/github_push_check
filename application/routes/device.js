/**
 * @swagger
 * tags:
 *   name: Devices
 *   description: Device management APIs
 */

/**
 * @swagger
 * /devices:
 *   get:
 *     summary: Retrieve all devices
 *     tags: [Devices]
 *     responses:
 *       200:
 *         description: A list of devices
 *       500:
 *         description: Server error
 */
app.get('/devices', (req, res) => {
  // Logic to retrieve devices
});

/**
 * @swagger
 * /devices:
 *   post:
 *     summary: Create a new device
 *     tags: [Devices]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name:
 *                 type: string
 *               type:
 *                 type: string
 *               location:
 *                 type: string
 *     responses:
 *       201:
 *         description: Device created
 *       400:
 *         description: Invalid input
 *       500:
 *         description: Server error
 */
app.post('/devices', (req, res) => {
  // Logic to create a device
});

/**
 * @swagger
 * /devices/{id}:
 *   delete:
 *     summary: Delete a device
 *     tags: [Devices]
 *     parameters:
 *       - name: id
 *         in: path
 *         required: true
 *         description: The device ID
 *         schema:
 *           type: string
 *     responses:
 *       204:
 *         description: Device deleted
 *       404:
 *         description: Device not found
 *       500:
 *         description: Server error
 */
app.delete('/devices/:id', (req, res) => {
  // Logic to delete a device
});
